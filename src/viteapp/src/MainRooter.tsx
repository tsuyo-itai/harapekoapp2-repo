import { Routes, Route } from "react-router-dom";
import './App.scss'
import App from './App.tsx';
import UserEditView from './views/UserEditView.tsx'
import PlanEditView from './views/admin/PlanEditView.tsx'

function MainRouter() {
  return (
    <>
      <Routes>
        <Route path="/">
          <Route index={true} element={<App/>}/>
          <Route path="edit" element={<UserEditView />} />
          {/* adminの階層 */}
          <Route path="admin">
            <Route index={true} element={<App/>}/>
            <Route path="subscription" element={<PlanEditView />} />
          </Route>
          {/* adminの階層 */}
        </Route>
      </Routes>
    </>
  );
}


export default MainRouter
