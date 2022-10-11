d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
