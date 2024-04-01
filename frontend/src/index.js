import React from 'react';
import {createRoot} from 'react-dom/client';
import App from './App';
import {Provider} from 'react-redux';
import authReducer from './reducers/authReducer';
import {ChakraProvider} from "@chakra-ui/react";
import {configureStore} from '@reduxjs/toolkit';


const store = configureStore({
    reducer: {
        auth: authReducer,
    },
});

createRoot(
    document.getElementById('root')
).render(
    <ChakraProvider>
        <Provider store={store}>
            <App/>
        </Provider>,
    </ChakraProvider>
)
