import {useSelector} from 'react-redux';
import {BrowserRouter as Router, Navigate, Route, Routes} from "react-router-dom";
import {Login} from "./components/Auth/Login";
import {PublicRoute} from "./components/Auth/PublicRoute";
import {Register} from "./components/Auth/Register";
import {NavBar} from "./components/Navbar/Navbar";
import {TaskDetail} from "./components/Task/TaskDetail";
import {TaskList} from "./components/Task/TaskList";
import {Flex, Spinner} from "@chakra-ui/react";
import {useEffect} from 'react';
import {useDispatch} from 'react-redux';
import {initialize} from './actions/authActions';
import {Authenticated} from "./components/Auth/Authenticated";

function App() {
    const authInitialized = useSelector(state => state.auth.isInitialized);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(initialize());
    }, [dispatch]);

    return (
        <Router>
            {!authInitialized ? (
                <Flex
                    height="100vh"
                    alignItems="center"
                    justifyContent="center"
                >
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Flex>
            ) : (
                <Routes>
                    <Route
                        path="/login"
                        element={
                            <PublicRoute>
                                <Login/>
                            </PublicRoute>
                        }
                    />
                    <Route
                        path="/register"
                        element={
                            <PublicRoute>
                                <Register/>
                            </PublicRoute>
                        }
                    />
                    <Route path="/" element={<NavBar/>}>
                        <Route path="/" element={
                            <Authenticated>
                                <TaskList/>
                            </Authenticated>
                        }
                        />
                        <Route path="/:taskId" element={
                            <Authenticated>
                                <TaskDetail/>
                            </Authenticated>
                        }
                        />
                    </Route>
                    <Route path="*" element={<Navigate to="/"/>}/>
                </Routes>
            )}
        </Router>
    );
}

export default App;