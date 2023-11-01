import React from 'react'
function getFullStar(color) {
  return <i style={{ color }}  className='fas fa-star'></i>
}
function getHalfStar(color) {
  return <i style={{ color }} className='fas fa-star-half-alt'></i>
}
function getBlankStart(color) {
  return <i style={{ color }} className='far fa-star'></i>
}
function Rating({value, text,color}) {
  return (
    <div className="rating">
      {[...Array(5)].map((e, i) => {
        if (value - (i) >= 1)
        {
          return getFullStar(color)
        }
        else if (value - (i) >= 0.5)
        {
          return getHalfStar(color)
        }
        else
        {
          return getBlankStart(color)
          }
      })}
       <span> {text && text}</span>
    </div>
  )
}


export default Rating