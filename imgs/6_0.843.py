d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.position_pen(3,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)

d.end()
