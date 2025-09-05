import { jwtDecode } from "jwt-decode"
import { dataStore } from "./store/data"



const BASE_URL = import.meta.env.VITE_API_URL

export async function callApi(endpoint, method = "GET", data = null) {
  try {
    const options = {
      method: method,
      headers: { "Content-Type": "application/json" },
      credentials: "include"
    }

    if (data && ["POST", "PUT", "PATCH"].includes(method)) {
      options.body = JSON.stringify(data)
    }

    const response = await fetch(`${BASE_URL}/${endpoint}`, options)
    const resData = await response.json()

    return {
      ok: response.ok,
      status: response.status,
      resData: resData
    }

  } catch (error) {
    console.error("API call failed:", error)
    return {
      ok: false,
      status: 500,
      data: { error: error.message || "Something went wrong!" }
    }
  }
}



export const getCookie = (key) => {
  const cookies = document.cookie.split("; ")
  for (const c of cookies) {
    const [k, v] = c.split("=")
    if (k == key) {
      return v;
    }
  }
  return null;
}


const DOMAIN_NAME = import.meta.env.VITE_DOMAIN_NAME

export const setCookie = (key, value, domain = DOMAIN_NAME, expireInSeconds = 86400) => {
  let cookieStr = `${encodeURIComponent(key)}=${encodeURIComponent(value)}; path=/;`;

  if (domain) {
    cookieStr += ` domain=${domain};`;
  }

  if (expireInSeconds) {
    const date = new Date();
    date.setTime(date.getTime() + expireInSeconds * 1000);
    cookieStr += ` expires=${date.toUTCString()};`;
  }

  document.cookie = cookieStr;
};


export const decodeToken = (token) => {
  try {
    const decoded = jwtDecode(token)
    return decoded
  }
  catch (error) {
    console.log(error)
    return null
  }
}


export const tokenChecker = () => {
  const token = getCookie("access_token_cookie")
  const decoded = decodeToken(token)
  if (decoded) {
    const data_store = dataStore()
    data_store.updateRole(decoded.role)
    data_store.updateUsername(decoded.sub)
    data_store.updateID(decoded.id)
    
  }
}

export const removeCookie = (key) => {
  document.cookie = `${encodeURIComponent(key)}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC;`;
};
