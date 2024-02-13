import React, { useState } from 'react';
import "../assets/stylesheets/Header.scss"
import { Link } from "react-router-dom";

function Header() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <>
      {/* ヘッダー */}
      <header>
        <div className="header-container">
          <div className="hamburger" onClick={toggleSidebar}>
            <div className="bar"></div>
            <div className="bar"></div>
            <div className="bar"></div>
          </div>
          <a href="/" className="header-logo">
            はらぺこ
          </a>
        </div>
      </header>

      {/* サイドバー */}
      <div className={`sidebar ${isSidebarOpen ? 'show-sidebar' : ''}`}>
        <ul className="nav-menu">
          <li>
            <a href="/">ランチパスポート</a>
            <span>使えるお店を探す</span>
          </li>
          <li>
            <a href="/">開発者ブログ</a>
          </li>
          <li>
            <Link to={`/edit`}>ユーザー情報編集</Link>
          </li>
        </ul>
      </div>

      {/* その他のコンテンツ */}
      {/* ... */}
    </>
  );
};

export default Header;
