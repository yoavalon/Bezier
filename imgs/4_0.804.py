d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)

d.end()
