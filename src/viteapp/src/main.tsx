import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.tsx'
import MainRouter from './MainRooter.tsx'
import './index.css'
import { BrowserRouter } from "react-router-dom";


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <MainRouter />
    </BrowserRouter>
  </React.StrictMode>,
)
