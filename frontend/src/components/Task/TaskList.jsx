import {Box, Center, Container, Spinner} from "@chakra-ui/react";
import {useEffect, useRef, useState} from "react";
import axiosInstance from "../../services/axios";
import {AddUpdateTaskModal} from "./AddUpdateTaskModal";
import {TaskCard} from "./TaskCard";
import {useSelector} from "react-redux";

export const TaskList = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);

    // const user = useSelector

    useEffect(() => {
        if (isMounted.current) return;
        fetchTasks();
        isMounted.current = true;
    }, []);

    const fetchTasks = () => {
        setLoading(true);
        axiosInstance
            .get("/task/assigned/{user_id}")
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
                        <TaskCard task={task} key={task.id}/>
                    ))}
                </Box>
            )}
        </Container>
    );
};