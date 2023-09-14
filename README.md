# Nex

ハッカソンに参加し、ゲーム専用の掲示板 Nex を作成しました。

# 開発環境

-   Node.js 18.17.1
-   Python 3.10.11

Docker の場合は以下のようなポート設定になっています。
| port | name | cotainer_name |
| - | - | - |
| 8000 | FastAPI | app-api |
| 3000 | Next.js | app-web |
| 5432 | PostgreSQL | app-db |
| 8001 | RedisInsight | app-redis-stack |
| 6379 | Redis | app-redis-stack |

# 環境構築

[wiki](https://github.com/geekcamp2023-vol9-team28/Nex/wiki)の手順にしたがって構築をしてください。
