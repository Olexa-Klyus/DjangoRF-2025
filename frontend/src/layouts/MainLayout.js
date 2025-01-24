import {Outlet} from "react-router-dom";
import HeaderComponent from "../components/HeaderComponent";

const MainLayout = () => {
    return (<>
        <div>
            <HeaderComponent/>
            <Outlet/>
        </div>
        <br/>
        <footer>
            СХІДНИЦЯ 2025
        </footer>
    </>);
};

export {MainLayout};