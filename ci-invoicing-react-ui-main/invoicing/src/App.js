import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom"
import InvoiceList from './components/InvoiceList/InvoiceList';
import InvoiceForm from "./components/InvoiceForm/InvoiceForm";
import InvoiceItems from "./components/InvoiceItems/InvoiceItems";
import ItemForm from "./components/ItemForm/ItemForm";
import Signin from './components/Signin/signin';
function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='signin' element={<Signin/>}>
        </Route>
        {/* <Route path='' element={<InvoiceList />}>
        </Route> */}
        <Route path='newInvoice' element={<InvoiceForm />}>
        </Route>
        <Route path='/:id' element={<InvoiceItems />}>
        </Route>
        <Route path='/:id/newItem' element={<ItemForm />}>
        </Route>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
