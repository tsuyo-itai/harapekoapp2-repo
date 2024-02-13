import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import "../assets/stylesheets/Base.scss"
import "../assets/stylesheets/Header.scss"
import Header from '../components/Header';


interface UserProfile {
  id: number;
  email: string;
  status: boolean;
  created_at: string;
  updated_at: string;
  first_name: string,
  last_name: string,
  date_of_birth: Date | null,
  phone_number: string,
  postal_code: string,
  prefecture: string,
  city: string,
  address: string,
  icon_image: string
}

const UserEditView = () => {
  const navigate = useNavigate();

  const [userprofile, setUserProfile] = useState<UserProfile>({
    id: 0,
    email: '',
    status: false,
    created_at: '',
    updated_at: '',
    first_name: '',
    last_name: '',
    date_of_birth: null,
    phone_number: '',
    postal_code: '',
    prefecture: '',
    city: '',
    address: '',
    icon_image: ''
  });

  const fetchUserProfileData = async () => {
    try {
      // GET リクエストを行う
      const response = await axios.get('http://localhost:8000/api/v1/user_with_profile/2');
      console.log(response);
      // 取得したデータを state に保存
      setUserProfile(response.data as UserProfile);

    } catch (error) {
      console.error('GET request failed', error);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setUserProfile((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleCancel = () => {
    if (window.confirm('変更を破棄してもよろしいですか？')) {
      // 1つ前に戻るボタンを押した挙動
      navigate(-1);
      console.log("キャンセルされました");
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // フォームの送信処理をここに追加
    console.log(userprofile);

    try {
      // PUTリクエストを送信
      const response = await axios.put('http://localhost:8000/api/v1/userprofile/2', userprofile);

      // リクエストが成功した場合の処理
      console.log('PUT request successful:', response.data);
      window.alert("変更が完了しました");
      // 1つ前に戻るボタンを押した挙動
      navigate(-1);
    } catch (error) {
      // エラーハンドリング
      console.error('PUT request failed:', error);
    }

  };

  useEffect(() => {
    fetchUserProfileData();
  }, []); // 空の依存リストを指定することで、コンポーネントがマウントされたときのみ実行

  return (
    <>
      <Header />
      <div className='main-container'>
        <form onSubmit={handleSubmit}>
          {/* 各フィールドの入力 */}
          <h4>名字</h4>
          <input
            type="text"
            name="first_name"
            value={userprofile.first_name}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>名前</h4>
          <input
            type="text"
            name="last_name"
            value={userprofile.last_name}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>生年月日</h4>
          <input
            type="date"
            name="date_of_birth"
            value={userprofile.date_of_birth ? new Date(userprofile.date_of_birth).toISOString().split('T')[0] : ''}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>電話番号</h4>
          <input
            type="text"
            name="phone_number"
            value={userprofile.phone_number}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>郵便番号</h4>
          <input
            type="text"
            name="postal_code"
            value={userprofile.postal_code}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>都道府県</h4>
          <input
            type="text"
            name="prefecture"
            value={userprofile.prefecture}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>市区町村</h4>
          <input
            type="text"
            name="city"
            value={userprofile.city}
            onChange={handleChange}
            className="form-text-box"
          />

          <h4>住所</h4>
          <input
            type="text"
            name="address"
            value={userprofile.address}
            onChange={handleChange}
            className="form-text-box"
          />

          {/* 送信ボタン */}
          <div className='flex-container'>
            <input type="submit" value="変更" className="submit-button" />
            <input type="button" value="キャンセル" className="submit-button-cancel" onClick={handleCancel}/>
          </div>
        </form>
      </div>
    </>
  );
};

export default UserEditView;
