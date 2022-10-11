d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,0)

d.end()
