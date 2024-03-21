import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';

export const PublicRoute = (props) => {
    const { children } = props;
    const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) {
            navigate('/', { replace: true });
        }
    }, [isAuthenticated, navigate]);

    return !isAuthenticated ? <>{children}</> : null;
}