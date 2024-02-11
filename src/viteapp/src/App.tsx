import { useState, useEffect } from 'react'
import axios from 'axios';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.scss'
import Header from './components/Header.tsx'

interface User {
  id: number;
  email: string;
  status: boolean;
  created_at: string;
  updated_at: string;
}

function App() {
  const [count, setCount] = useState(0)
  // const [userList, setUserList] = useState<User[]>([]);
  const [user, setUser] = useState<User>({
    id: 0,
    email: '',
    status: false,
    created_at: '',
    updated_at: ''
  });

  const fetchUserData = async () => {
    try {
      // GET リクエストを行う
      const response = await axios.get('http://localhost:8000/api/v1/user/1');
      console.log(response);
      // 取得したデータを state に保存
      // setUserList(response.data);
      setUser(response.data as User);

    } catch (error) {
      console.error('GET request failed', error);
    }
  };

  useEffect(() => {
    fetchUserData();
  }, []); // 空の依存リストを指定することで、コンポーネントがマウントされたときのみ実行

  return (
    <>
      <Header />
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={fetchUserData}>Send POST Request</button>
        <div>
          {user.status ? (
            // ユーザーが存在する場合
            <div key={user.id}>
              <h3>ようこそ {user.email} さん</h3>
              <p>Created at: {user.created_at}</p>
            </div>
          ) : (
            // ユーザーが存在しない場合
            <p>ユーザーが存在しません。</p>
          )}
        </div>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
