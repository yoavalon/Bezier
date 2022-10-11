d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)

d.end()
