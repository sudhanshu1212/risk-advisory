
import React, { useState, useEffect } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Link, NavLink } from "react-router-dom";


const NavBarMenu = () => {
    return (

        <div>
            <Navbar bg="light" expand="lg">
                
                    <Navbar.Brand href="#home">Equities</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    
                        <Nav className="me-auto">
                            <NavLink className="show-products-nav"  to="/">Equities</NavLink>
                            <NavLink className="add-product-nav"  to="/addEquities">Add Equities</NavLink>
                            <NavLink className="add-product-nav"  to="/csv">Add csv </NavLink>
                            <NavLink className="add-product-nav"  to="/graphs">see graph</NavLink>
                        </Nav>
                    
                
            </Navbar>
        </div>
    );
};
export default NavBarMenu;