import React, { useEffect } from 'react'
import { Col, Row } from 'react-bootstrap'
import { useSelector,useDispatch } from 'react-redux';
import Product from '../components/Product';
import { listProducts } from '../actions/productAction';
import Loader from '../components/Loader';
import Message from '../components/Message';
import { useLocation, useSearchParams } from 'react-router-dom';
import Paginate from '../components/Paginate';
import ProductCarousel from '../components/ProductCarousel';

function HomeScreen() {
  // const [products, setProducts] = useState([])
  const dispatch = useDispatch();
  const productList = useSelector(state => state.productList)
  const { error, loading, products,page,pages } = productList;

  const location = useLocation();
  let keyword = location.search
  useEffect(() => {
    dispatch(listProducts(keyword))
    console.log(keyword)
   
},[dispatch,keyword])

  return (
    <div>
      {!keyword && <ProductCarousel />}
      <h1>Latest Products</h1>
      {loading ?<Loader/>: error ? <Message variant='danger'>{error}</Message> :
       
      <div>
        <Row>
          {products && products.map(product => (
            <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
              <Product product={product} /></Col>
          ))}
          </Row>
          <Paginate page={page} pages={pages} keyword={keyword} />
          </div>
      }
    </div>
  )
}

export default HomeScreen