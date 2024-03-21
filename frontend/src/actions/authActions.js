import axiosInstance from "../services/axios";
import {validateToken} from "../utils/jwt";
import Cookies from 'js-cookie';

export const initialize = () => async (dispatch) => {
    try {
        const accessToken = Cookies.get("accessToken");

        if (accessToken && validateToken(accessToken)) {
            axiosInstance.defaults.headers.common["Authorization"] = `Bearer ${accessToken}`;
            const response = await axiosInstance.get("/api/v1/user/me");
            const {data: user} = response;

            dispatch({
                type: "INITIALIZE",
                payload: {
                    isAuthenticated: true,
                    user,
                },
            });
        } else {
            dispatch({
                type: "INITIALIZE",
                payload: {
                    isAuthenticated: false,
                    user: null,
                },
            });
        }
    } catch (error) {
        console.error(error);
        dispatch({
            type: "INITIALIZE",
            payload: {
                isAuthenticated: false,
                user: null,
            },
        });
    }
};

export const login = (email, password) => async (dispatch) => {
    const formData = new FormData()
    formData.append("username", email)
    formData.append("password", password)
    const response = await axiosInstance.post("/auth/login", formData);

    Cookies.set("accessToken", response.data.access_token);
    Cookies.set("refreshToken", response.data.refresh_token);

    axiosInstance.defaults.headers.common["Authorization"] = `Bearer ${Cookies.get("accessToken")}`;

    const userResponse = await axiosInstance.get("/user/me");
    const {data: user} = userResponse;

    dispatch({
        type: "LOGIN",
        payload: {
            user,
        },
    });
};

export const logout = () => {
    Cookies.remove("accessToken");
    Cookies.remove("refreshToken");

    return {
        type: "LOGOUT",
    };
};