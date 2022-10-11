d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
