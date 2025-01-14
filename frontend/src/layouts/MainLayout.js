import {Link, Outlet} from "react-router-dom";

const MainLayout = () => {
    return (<>
        <header>
            <Link to="/register">  RegisterPage   </Link>
            <Link to="/login">  LoginPage   </Link>
            <Link to="/adverts">   AdvertsPage   </Link>
            <Link to="/chat">   ChatPage   </Link>
        </header>
        <br/>
        <div>
            <Outlet/>
        </div>
        <br/>
        <footer>
            2025
        </footer>
    </>);
};

export {MainLayout};