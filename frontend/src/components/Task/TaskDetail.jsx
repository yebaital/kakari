import {
    Button,
    Center,
    Container,
    Spinner,
    Text,
    useColorModeValue,
    useToast,
} from "@chakra-ui/react";
import {useEffect, useRef, useState} from "react";
import {useNavigate, useParams} from "react-router-dom";
import axiosInstance from "../../services/axios";
import {AddUpdateTaskModal} from "./AddUpdateTaskModal";

export const TaskDetail = () => {
    const [task, setTask] = useState({});
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    const {taskId} = useParams();
    const navigate = useNavigate();
    const toast = useToast();
    const background = useColorModeValue("gray.300", "gray.600");

    useEffect(() => {
        if (isMounted.current) return;
        fetchTask();
        isMounted.current = true;
    }, [taskId]);

    const fetchTask = () => {
        setLoading(true);
        axiosInstance
            .get(`/task/${taskId}`)
            .then((res) => {
                setTask(res.data);
            })
            .catch((error) => console.error(error))
            .finally(() => {
                setLoading(false);
            });
    };

    const deleteTask = () => {
        setLoading(true);
        axiosInstance
            .delete(`/task/${taskId}`)
            .then(() => {
                toast({
                    title: "Task deleted successfully",
                    status: "success",
                    isClosable: true,
                    duration: 1500,
                });
                navigate("/");
            })
            .catch((err) => {
                console.error(err);
                toast({
                    title: "Couldn't delete task",
                    status: "error",
                    isClosable: true,
                    duration: 2000,
                });
            })
            .finally(() => setLoading(false));
    };

    if (loading) {
        return (
            <Container mt={6}>
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            </Container>
        );
    }

    return (
        <>
            <Container mt={6}>
                <Button
                    colorScheme="gray"
                    onClick={() => navigate("/", {replace: true})}
                >
                    Back
                </Button>
            </Container>
            <Container
                bg={background}
                minHeight="7rem"
                my={3}
                p={3}
                rounded="lg"
                alignItems="center"
                justifyContent="space-between"
            >
                <Text fontSize={22}>{task.title}</Text>
                <Text bg="gray.500" mt={2} p={2} rounded="lg">
                    {task.description}
                </Text>
                <AddUpdateTaskModal
                    my={3}
                    editable={true}
                    defaultValues={{
                        title: task.title,
                        description: task.description,
                        status: task.status,
                    }}
                    onSuccess={fetchTask}
                />
                <Button
                    isLoading={loading}
                    colorScheme="red"
                    width="100%"
                    onClick={deleteTask}
                >
                    Delete
                </Button>
            </Container>
        </>
    );
};