d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)

d.end()
