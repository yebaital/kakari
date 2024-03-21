const initialState = {
    isAuthenticated: false,
    isInitialized: false,
    user: null,
};

function authReducer(state = initialState, action) {
    switch (action.type) {
        case "INITIALIZE":
            return {
                ...state,
                isAuthenticated: action.payload.isAuthenticated,
                isInitialized: true,
                user: action.payload.user,
            };

        case "LOGIN":
            return {
                ...state,
                isAuthenticated: true,
                user: action.payload.user,
            };

        case "LOGOUT":
            return {
                ...state,
                isAuthenticated: false,
                user: null,
            };

        default:
            return state;
    }
}

export default authReducer;