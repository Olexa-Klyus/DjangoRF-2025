import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const advertService = {
    getAll() {
        return apiService.get(urls.adverts)
    },
    create(data) {
        return apiService.post(urls.adverts, data)
    }
}

export {
    advertService
}