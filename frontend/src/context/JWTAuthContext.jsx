import {createContext, useEffect, useReducer, useRef} from "react";
import {validateToken} from "../utils/jwt"
import {resetSession, setSession} from "../utils/session";
import axiosInstance from "../services/axios";

/**
 * Represents the initial state of an application.
 * @typedef {object} initialState
 * @property {boolean} isAuthenticated - Indicates whether the user is authenticated.
 * @property {boolean} isInitialized - Indicates whether the application has been initialized.
 * @property {object|null} user - Represents the user object or null if no user is logged in.
 */
const initialState = {
    isAuthenticated: false,
    isInitialized: false,
    user: null
}

export const AuthContext = createContext({
    ...initialState,
    login: () => Promise.resolve(),
    logout: () => Promise.resolve()
})

/**
 * Handlers for different actions.
 * @typedef {Object} Handlers
 * @property {function} INITIALIZE - Handler for initializing the state.
 * @property {function} LOGIN - Handler for handling login action.
 * @property {function} LOGOUT - Handler for handling logout action.
 */
const handlers = {
    INITIALIZE: (state, action) => {
        const {isAuthenticated, user} = action.payload

        return {
            ...state,
            isAuthenticated,
            isInitialized: true,
            user,
        }
    },
    LOGIN: (state, action) => {
        const {user} = action.payload;

        return {
            ...state,
            isAuthenticated: true,
            user,
        }
    },
    LOGOUT: (state) => {
        return {
            ...state,
            isAuthenticated: false,
            user: null
        }
    }
}

/**
 * Reduces the state based on the action type.
 *
 * @param {Object} state - The current state.
 * @param {Object} action - The action to be performed.
 * @returns {Object} - The new state.
 */
const reducer = (state, action) => handlers[action.type] ? handlers[action.type](state, action) : state;

/**
 * A utility class for managing authentication.
 *
 * @param {Object} props - The props passed to the AuthProvider.
 * @param {ReactNode} props.children - The child components of the AuthProvider.
 * @returns {Function} - The AuthProvider function.
 */
export const AuthProvider = (props) => {
    const {children} = props
    const [state, dispatch] = useReducer(reducer, initialState)

    const isMounted = useRef(false);

    useEffect(() => {
        if (isMounted.current) return
        const initialize = async () => {
            try {
                const accessToken = localStorage.getItem("accessToken")
                if (accessToken && validateToken(accessToken)) {
                    setSession(accessToken)

                    const response = await axiosInstance.get("/api/v1/user/me")
                    //it's "data" in the response, we are renaming it to user
                    const {data: user} = response
                    dispatch({
                        type: "INITIALIZE",
                        payload: {
                            isAuthenticated: true,
                            user
                        }
                    })
                } else {
                    dispatch({
                        type: "INITIALIZE",
                        payload: {
                            isAuthenticated: false,
                            user: null
                        }
                    })
                }
            } catch (error) {
                console.error(error)
                dispatch({
                    type: "INITIALIZE",
                    payload: {
                        isAuthenticated: false,
                        user: null
                    }
                })
            }
        }
        initialize()
        isMounted.current = true
    }, []);

    const getTokens = async (email, password) => {
        const formData = new FormData()
        formData.append("username", email)
        formData.append("password", password)
        try {
            const response = await axiosInstance.post("/auth/login", formData)
            setSession(response.data.access_token, response.data.refresh_token)
        } catch (error) {
            throw error
        }
    }

    const login = async (email, password) => {
        try {
            await getTokens(email, password)
            const response = await axiosInstance.get("/user/me")
            const {data: user} = response
            dispatch({
                type: "LOGIN",
                payload: {
                    user
                }
            })
        } catch (error) {
            return Promise.reject(error)
        }
    }

    const logout = () => {
        resetSession()
        dispatch({type: "LOGOUT"})
    }

    return <AuthContext.Provider value={{
        ...state,
        login,
        logout
    }}>
        {children}
    </AuthContext.Provider>

}

export const AuthConsumer = AuthContext.Consumer