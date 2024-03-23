import {
    Button,
    Drawer,
    DrawerBody,
    DrawerContent,
    DrawerHeader,
    DrawerOverlay,
    Flex,
    List,
    ListItem
} from "@chakra-ui/react";
import { Icon  } from "@chakra-ui/icons";
import {FaUser, FaTasks} from "react-icons/fa";

const menuItems = [
    { id: 1, name: 'Dashboard', icon: <Icon as={FaUser} /> },
    { id: 2, name: 'Item 2', icon: <Icon as={FaTasks} /> },
];
export const Sidebar = () => (
    <Flex flexGrow={1} overflow="auto">
        {/* Sidebar */}
        <Button onClick={onOpen}>Open sidebar</Button>
        <Drawer isOpen={isOpen} placement="left" onClose={onClose}>
            <DrawerOverlay>
                <DrawerContent>
                    <DrawerHeader>Sidebar</DrawerHeader>
                    <DrawerBody>
                        <List spacing={3} color="white">
                            {menuItems.map(item => (
                                <ListItem key={item.id} alignItems="center">
                                    <Icon as={item.icon} />
                                    {item.name}
                                </ListItem>
                            ))}
                        </List>
                    </DrawerBody>
                </DrawerContent>
            </DrawerOverlay>
        </Drawer>
    </Flex>
);