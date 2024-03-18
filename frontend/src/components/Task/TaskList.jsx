import {Box, Center, Container, Spinner} from "@chakra-ui/react";
import {useEffect, useRef, useState} from "react";
import axiosInstance from "../../services/axios";
import {AddUpdateTaskModal} from "./AddUpdateTaskModal";
import {TodoCard} from "./TaskCard";

export const TodoList = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);

    useEffect(() => {
        if (isMounted.current) return;
        fetchTasks();
        isMounted.current = true;
    }, []);

    const fetchTasks = () => {
        setLoading(true);
        axiosInstance
            .get("/task/")
            .then((res) => {
                setTasks(res.data);
            })
            .catch((error) => {
                console.error(error);
            })
            .finally(() => {
                setLoading(false);
            });
    };

    return (
        <Container mt={9}>
            <AddUpdateTaskModal onSuccess={fetchTasks}/>
            {loading ? (
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            ) : (
                <Box mt={6}>
                    {tasks?.map((task) => (
                        <TodoCard todo={task} key={task.id}/>
                    ))}
                </Box>
            )}
        </Container>
    );
};