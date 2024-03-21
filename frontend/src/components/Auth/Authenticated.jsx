import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';

export const Authenticated = (props) => {
    const { children } = props;
    const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
    const navigate = useNavigate();

    useEffect(() => {
        if (!isAuthenticated) {
            navigate('/login', { replace: true });
        }
    }, [isAuthenticated, navigate]);

    return isAuthenticated ? <>{children}</> : null;
}