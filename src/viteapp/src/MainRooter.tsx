import { Routes, Route } from "react-router-dom";
import './App.scss'
import App from './App.tsx';
import UserEditView from './views/UserEditView.tsx'

function MainRouter() {

  return (
    <>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/edit" element={<UserEditView />} />
      </Routes>
    </>
  )
}

export default MainRouter
