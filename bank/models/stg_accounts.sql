{{config(
    materialized='table',
    tags=['painel_contas']
    )}}

select * from {{source('mysql','accounts')}}