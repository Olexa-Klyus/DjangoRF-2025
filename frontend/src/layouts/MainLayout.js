import {Link, Outlet} from "react-router-dom";

const MainLayout = () => {
    return (<>
        <header>
            <Link to="/login">  LoginPage   </Link>
            <Link to="/adverts">   AdvertsPage   </Link>
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