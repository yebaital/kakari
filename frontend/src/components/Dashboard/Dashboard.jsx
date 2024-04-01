import {useEffect, useRef, useState} from "react";
import {useSelector} from "react-redux";
import {Box, CircularProgress, Flex} from "@chakra-ui/react";
import axiosInstance from "../../services/axios";

export const Dashboard = () => {
    const [isCollapsed, setIsCollapsed] = useState(false);
    const [loading, setLoading] = useState(true);
    const [tasks, setTasks] = useState({});
    const isMounted = useRef(false);
    const userId = useSelector(state => state.auth.user && state.auth.user.user_id);

    useEffect(() => {
        if (isMounted.current) return;
        console.log(userId)
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

    const mainContentMargin = isCollapsed ? "0px" : "250px";

    return (
        <Flex direction="row" h="100vh">
            {/* Main Content */}
            <Box marginLeft={mainContentMargin}>
                {/* Add your dashboard content here */}
                {loading
                    ? <CircularProgress isIndeterminate color="green.300" />
                    : Object.entries(tasks).map(([key, task]) => (
                        <Box key={key} p={3} shadow="md" borderWidth="1px">
                            {task.title}
                        </Box>
                    ))
                }
            </Box>
        </Flex>
    )
}