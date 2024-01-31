import request from '@/utils/system/request'



export function getCommentApi(name: string) {
  return request({
    url: '/comment?name='+name,
    method: 'get',
  })
}


export function getCommentTypeApi(name: string) {
  return request({
    url: '/comment_type?name='+name,
    method: 'get',
  })
}


export function getCiYunApi(name: string) {
  return request({
    url: '/ciyun?name='+name,
    method: 'get',
  })
}


export function addCommentApi(data: any) {
  return request({
    url: '/add/comment',
    method: 'post',
    data
  })
}


export function addOpinionApi(data: any) {
  return request({
    url: '/add/opinion',
    method: 'post',
    data
  })
}



export function getOpinionApi(name: string) {
  return request({
    url: '/opinion?software='+name,
    method: 'get',
  })
}





export function analysisCommentApi(data:any) {
  return request({
    url: '/analysis/comment',
    method: 'post',
    data
  })
}

