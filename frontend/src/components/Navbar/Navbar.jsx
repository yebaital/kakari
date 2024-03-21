import {Box, Button, Flex, Stack, Text, useColorModeValue} from "@chakra-ui/react";
import {Outlet} from "react-router-dom";
import {useDispatch} from 'react-redux';
import {logout} from '../../actions/authActions'

export const NavBar = () => {
    const dispatch = useDispatch();
    const handleLogout = () => {
        console.log("Logging out...");
        dispatch(logout());
    }
    return (
        <Box minHeight="100vh">
            <Flex
                as="nav"
                align="center"
                justify="space-between"
                wrap="wrap"
                padding="1rem"
                bg={useColorModeValue("green.300", "green.600")}
                color="white"
            >
                <Text as="h2" fontSize={24} fontWeight="bold">
                    KAKARI
                </Text>
                <Stack direction="row" align="center" spacing={4}>
                    <Button onClick={handleLogout} colorScheme="green">
                        Logout
                    </Button>
                </Stack>
            </Flex>
            <Outlet/>
        </Box>
    );
};