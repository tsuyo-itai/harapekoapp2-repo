import React, { useState } from 'react';
import "../assets/stylesheets/Header.scss"

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
            <a href="/">ツールTOP</a>
          </li>
          <li>
            <a href="/">開発者ブログ</a>
          </li>
          <li>
            <a href="/">お問い合わせ</a>
          </li>
        </ul>
      </div>

      {/* その他のコンテンツ */}
      {/* ... */}
    </>
  );
};

export default Header;
