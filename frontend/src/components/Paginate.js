import React from 'react'
// import { Pagination } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import Pagination from 'react-bootstrap/Pagination';

import { Link } from 'react-router-dom'

function Paginate({ pages, page, keyword = '', isAdmin = false }) {
   if (keyword) {
        keyword = keyword.split('?keyword=')[1].split('&')[0]
  }

  console.log(isAdmin)
  return (pages > 1 && (
        <Pagination>
      {[...Array(pages).keys()].map((x) => (
        <Link key={x + 1}
        to={!isAdmin ? {
          pathname: `/`,
          hash: "",
          search: `?keyword=${keyword}&page=${x + 1}`, 
        } :
          {
          pathname: `/admin/productlist/`,
          hash: "",
          search: `?keyword=${keyword}&page=${x + 1}`, 
        }
      }
      >

          <p active={x + 1 === page} className={x+1 === page?`paginate-items active`:`paginate-items `}>
            {x + 1}
          </p>
   
      </Link>
        // <Link to={`/?keyword=${keyword}&page=${x + 1}`}   key={x + 1}>
        //   <Pagination.Item active={x + 1 === page}>{x+1}</Pagination.Item>
        // </Link>
      ))}
        </Pagination>
    )
    )
}

export default Paginate