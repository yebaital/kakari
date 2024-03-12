import {Button} from "@chakra-ui/react";

const StyledButton = ({children, onClick, ...props}) => {
    const sharedStyles = {
        cursor: 'pointer',
        width: '352px',
        height: '56px',
        padding: '0px 8px',
        border: '1px solid #ffffff',
        boxSizing: 'border-box',
        borderRadius: '12px',
        backgroundColor: '#161616',
        color: '#ffffff',
        fontSize: '16px',
        fontFamily: 'Poppins',
        fontWeight: '500',
        lineHeight: '20px',
        outline: 'none',
        _hover: {
            backgroundColor: '#017BD6', // color of the left column
        }
    };

    return (
        <Button sx={sharedStyles} onClick={onClick} {...props}>
            {children}
        </Button>
    );
};

export default StyledButton;