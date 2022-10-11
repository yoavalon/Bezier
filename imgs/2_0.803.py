d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,1)
d.position_pen(1,1)

d.end()
