import {AdvertForm} from "../components/AdvertForm";
import {AdvertsComponent} from "../components/AdvertsComponent";
import {Chat} from "../components/Chat";

const AdvertsPage = () => {
    return (
        <div>
            {/*<AdvertForm/>*/}
            <hr/>
            <AdvertsComponent/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {AdvertsPage};