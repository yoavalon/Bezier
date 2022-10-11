d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,3)

d.end()
