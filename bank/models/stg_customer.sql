{{config(materialized='table')}}

select * from {{source('mysql','customers')}}