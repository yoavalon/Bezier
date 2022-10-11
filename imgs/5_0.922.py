d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.SW, Length.long)

d.end()
