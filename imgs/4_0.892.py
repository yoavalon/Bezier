d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
