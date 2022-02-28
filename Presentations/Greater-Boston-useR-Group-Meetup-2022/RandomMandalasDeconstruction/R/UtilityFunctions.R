
#' Par image grid.
#' @description Plots image arrays with \code{\link{image} using \code{\linl{par}}.
#' @param imageArrays A list of image arrays.
#' @param mfrow Same as \code{mfrow} of \code{par}.
#' @details If the \code{imageArrays} does not have names, then 
#' index ordinals are automatically assigned.
#' @return Nothing.
ParImageGrid <- function( imageArrays, mfrow = NULL, ...) {
  
  if( !is.list(imageArrays) ) {
    stop("The first argument is expected to be a list of numerical 2D arrays.")
  }
  
  if( is.null(mfrow) ) {
    mfrow = c( ceiling(imageArrays / 5), 5 )
  }
  
  if( is.null(names(imageArrays)) ) {
    names(imageArrays) <- 1:length(imageArrays)
  }
  
  par( mfrow = mfrow, mai = c(0,0,0,0), ...)
  for(i in 1:length(imageArrays)){
    image( imageArrays[[i]], axes = FALSE, col = gray( 0:255 / 255 ) )
    text( 0.2, 0, names(imageArrays)[[i]], cex = 1.2, col = 2, pos = c(3,4))
  }
  
}