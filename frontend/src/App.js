import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import ShowEquities from './components/ShowEquities';
import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom';
import  NavBarMenu from './components/NavBarMenu';
import AddEquities from './components/AddEquities';
import EquitiesDetail from './components/EquitiesDetail';
import UpdateEquities from './components/UpdateEquities';
function App() {
  return (
    <div className="App">
      <Router>
        <NavBarMenu/>
        <Routes>
          <         Route path="/" element={<ShowEquities />} />
        </Routes>

        <Routes>
          <         Route path="/addEquities" element={<AddEquities />} />
        </Routes>
        <Routes>
          <         Route path="/:id/" element={<EquitiesDetail />} />
        </Routes>
        <Routes>
          <         Route path="/:id/update" element={<UpdateEquities />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
