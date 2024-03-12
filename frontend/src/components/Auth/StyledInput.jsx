import { Input } from "@chakra-ui/react";

const StyledInput = ({ placeholder, type, size = 'lg', register, marginTop = '6' }) => {
    const sharedStyles = {
        width: '352px',
        height: '48px',
        padding: '0px 8px',
        border: '1px solid #363636',
        boxSizing: 'border-box',
        borderRadius: '12px',
        backgroundColor: '#1d1d1d',
        color: '#bcbcbc',
        fontSize: '16px',
        fontFamily: 'Poppins',
        lineHeight: '20px',
    };

    return (
        <Input
            placeholder={placeholder}
            type={type}
            size={size}
            mt={marginTop}
            sx={sharedStyles}
            {...register}
        />
    );
};

export default StyledInput;