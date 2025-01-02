import axios from "axios";

// const token = localStorage.getItem("accessToken");
// Base Axios instance
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1/',  // Your Django API URL
  headers: {
    'Content-Type': 'application/json',
  },
});

// Get all households
export const getHouseholds = async () => {
  const response = await api.get("households/");
  return response.data;
};

// Create a household
export const createHousehold = async (data) => {
  const response = await api.post("households/", data);
  return response.data;
};
