import {Box, Center, Container, Spinner, Text} from "@chakra-ui/react"; // Add Box, Text for rendering task title
import {useEffect, useRef, useState} from "react";
import {useSelector} from "react-redux";
import axiosInstance from "../../services/axios";

export const Dashboard = () => {

    const [loading, setLoading] = useState(true);
    const [tasks, setTasks] = useState({});
    const isMounted = useRef(false);


    const userId = useSelector(state => state.auth.user && state.auth.user.id);
    const user = useSelector(state => state.auth.user );

    useEffect(() => {
        if (user) console.log(user)


    }, []);

    useEffect(() => {
        if (isMounted.current) return;
        fetchTasks();
        isMounted.current = true;
    }, [userId]);

    const fetchTasks = async () => {
        setLoading(true)
        try {
            const res = await axiosInstance.get(`/task/assigned/${userId}`);
            console.log(res.data);
            setTasks(res.data);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    }

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
            {Object.entries(tasks).map(([key, task]) => (
                <Box key={key} p={3} shadow="md" borderWidth="1px">
                    <Text>
                        {task.title}
                    </Text>
                </Box>
            ))}
        </>
    )
}
