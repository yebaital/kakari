import {Box, Button, Flex, List, Text} from "@chakra-ui/react";
import {FaBars, FaTasks, FaUser, FaBoxes} from "react-icons/fa";
import {Icon} from "@chakra-ui/icons";
import {ProfileCard} from "./ProfileCard";

export const Sidebar = ({isCollapsed, onToggleCollapse}) => {

    const menuItems = [
        {id: 1, name: 'Dashboard', icon: FaUser},
        {id: 2, name: 'My Tasks', icon: FaTasks},
        {id: 3, name: 'Projects', icon: FaBoxes},
    ];

    if (isCollapsed) {
        // Sidebar collapsed: render only icons
        return (
            <Flex direction="column" px="12px" height="100vh" backgroundColor="#282828" color="#ffffff"
                  alignItems={"center"}>
                <Button onClick={() => {
                    onToggleCollapse();
                }} mb={3} p={0} backgroundColor="#282828" color="#ffffff" _hover={{bg: "#017bd6", color: "white"}}>
                    <FaBars/>
                </Button>
                {menuItems.map(item => (
                    <Icon fontSize="20px" as={item.icon} mb={8}/>
                ))}
            </Flex>
        );
    }

    // Sidebar not collapsed: render full content
    return (
        <Box backgroundColor="#282828" height="100vh" px="12px">
            <Button onClick={onToggleCollapse} p={0} mb={1} backgroundColor="#282828" color="#ffffff"
                    _hover={{bg: "#017bd6", color: "white"}}>
                <FaBars/>
            </Button>
            <Box w="100%" p={1}>
                <ProfileCard name="Yousef Baitalmal" email="ybaitalmal@panda.com.sa"
                             imgSrc={`${process.env.PUBLIC_URL}/hourglass.png`}/>
            </Box>
            <List spacing={3} color="#ffffff">
                {menuItems.map(item => (
                    <Flex alignItems="center" w="200px" p="12px">
                        <Box as={item.icon} fontSize="20px" mr={2}/>
                        <Text>{item.name}</Text>
                    </Flex>
                ))}
            </List>
        </Box>
    );
};