{{config(
    materialized='table',
    tags=['painel_usuarios']
    )}}


select * from {{source('mysql','customers')}}