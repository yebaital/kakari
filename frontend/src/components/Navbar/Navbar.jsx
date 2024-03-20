import { useAuth } from "../../hooks/useAuth";
import {Box, Button, Flex, Stack, useColorModeValue, Text} from "@chakra-ui/react";
import {Outlet} from "react-router-dom";

export const NavBar = () => {
    const { logout } = useAuth();
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
                    <Button onClick={logout} colorScheme="green">
                        Logout
                    </Button>
                </Stack>
            </Flex>
            <Outlet />
        </Box>
    );
};