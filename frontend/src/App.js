import {Flex, Spinner} from "@chakra-ui/react";
import {
    BrowserRouter as Router,
    Navigate,
    Route,
    Routes,
} from "react-router-dom";
import {Authenticated} from "./components/Auth/Authenticated";
import {Login} from "./components/Auth/Login";
import {PublicRoute} from "./components/Auth/PublicRoute";
import {Register} from "./components/Auth/Register";
import {NavBar} from "./components/Navbar/Navbar";
import {TaskDetail} from "./components/Task/TaskDetail";
import {TaskList} from "./components/Task/TaskList";
import {AuthConsumer, AuthProvider} from "./context/JWTAuthContext";

function App() {
    return (
        <>
            <AuthProvider>
                <Router>
                    <AuthConsumer>
                        {(auth) =>
                            !auth.isInitialized ? (
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
                                        <Route
                                            path="/"
                                            element={
                                                <Authenticated>
                                                    <TaskList/>
                                                </Authenticated>
                                            }
                                        />
                                        <Route
                                            path="/:todoId"
                                            element={
                                                <Authenticated>
                                                    <TaskDetail/>
                                                </Authenticated>
                                            }
                                        />
                                    </Route>
                                    <Route path="*" element={<Navigate to="/"/>}/>
                                </Routes>
                            )
                        }
                    </AuthConsumer>
                </Router>
            </AuthProvider>
        </>
    );
}

export default App;