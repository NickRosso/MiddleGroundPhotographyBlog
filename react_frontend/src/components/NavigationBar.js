import React from 'react';
import { Routes, Route, BrowserRouter as Router } from 'react-router-dom';
import Work from "./Work"
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

export default class NavigationBar extends React.Component {
  constructor(props) {
    super(props);
  render()
    return (
      <div>
        <Router>
          <Navbar color="light" light expand="md">
            <NavbarBrand href="/">MiddleGround PhotoG</NavbarBrand>
              <Nav className="mr-auto" navbar>
                <NavItem>
                  <NavLink href="/work">Work</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/about">About</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="https://www.instagram.com/nicholas.rosso/">Instagram</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="https://github.com/NickRosso">GitHub</NavLink>
                </NavItem>
              </Nav>
          </Navbar>
          <Routes>
            <Route path="/work" element={<Work/>} />
          </Routes>
        </Router>
      </div>
    );
}